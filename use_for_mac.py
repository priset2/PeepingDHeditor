from os import environ, urandom, unlink
from os.path import exists
from pathlib import Path
from base64 import b64encode, b64decode
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Protocol.KDF import PBKDF2
from json import loads, dumps

user_name = environ.get("USER") or Path.home().name
defaultSavePath = (
    f"/Applications/Peeping Dorm Manager.app/Contents/SharedSupport/prefix/drive_c/users/"
    f"{user_name}/AppData/LocalLow/Horny Doge/Peeping Dorm Manager"
)
savePath = environ.get("PDM_SAVE_PATH", defaultSavePath)
fileName = "GameSave_0.dat"
password = "PeepingHG20221124"

if not exists(savePath):
    raise FileNotFoundError(
        "Save path not found. Set PDM_SAVE_PATH to your game save directory."
    )

if not exists(f"{savePath}/{fileName}") and not exists(f"{savePath}/decrypted.json"):
    raise FileNotFoundError(
        f"Neither {fileName} nor decrypted.json exists under: {savePath}"
    )

if exists(f'{savePath}/decrypted.json'):
    with open(f'{savePath}/decrypted.json', 'r', encoding='utf-8') as f:
        data = loads(f.read())
    data['datas'] = [each | {'data': dumps(each['data'], separators=(',', ':'), ensure_ascii=False)} for each in data['datas']]
    iv = urandom(8)
    key = PBKDF2(password, iv, 8)
    cipher = DES.new(key, DES.MODE_CBC, iv)
    data = cipher.encrypt(pad(dumps(data, separators=(',', ':'), ensure_ascii=False).encode(), 8))
    with open(f'{savePath}/{fileName}', 'wb') as f:
        f.write(b64encode(iv + data))
    unlink(f'{savePath}/decrypted.json')
    print("✅ 加密完成！已覆盖游戏存档")
else:
    with open(f'{savePath}/{fileName}', 'r') as f:
        data = b64decode(f.read())
    iv, data = data[:8], data[8:]
    key = PBKDF2(password, iv, 8)
    cipher = DES.new(key, DES.MODE_CBC, iv)
    data = loads(unpad(cipher.decrypt(data), 8))
    data['datas'] = [each | {'data': loads(each['data'])} for each in data['datas']]
    with open(f'{savePath}/decrypted.json', 'w', encoding='utf-8') as f:
        f.write(dumps(data, ensure_ascii=False, indent=4))
    print("✅ 解密完成！请编辑 decrypted.json")
