import zipfile
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def manifestTransformation() -> str:
    manifest_json_file = open(str(BASE_DIR) + '/pointer/data/manifest.json')
    manifest_code = manifest_json_file.read()
    manifest_json_file.close()
    return manifest_code


def pointerTransformation() -> str:
    pointer_js_file = open(str(BASE_DIR) + '/pointer/data/script.js')
    pointer_js_code = pointer_js_file.read()
    pointer_js_file.close()
    return pointer_js_code


def injectScript() -> str:
    with open(f'{BASE_DIR}/pointer/data/inject.js') as injectJsFile:
        injectScriptCode = injectJsFile.read()
        return injectScriptCode


def makePointer() -> str:
    extensionName = 'Pointer'
    extensionPath = f'{BASE_DIR}/release/{extensionName}.zip'
    with zipfile.ZipFile(extensionPath, 'w') as zp:
        zp.writestr("manifest.json", manifestTransformation())
        zp.writestr("script.data", pointerTransformation())
        zp.writestr("inject.data", injectScript())
    return extensionPath
