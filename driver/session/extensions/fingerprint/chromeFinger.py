import zipfile
from pathlib import Path
from data.canvas import canvasSerialization
from data.platform import platformSerialization
from data.webGL import webGLSerialization


class Fingerprint:
    __base_dir = Path(__file__).resolve().parent.parent
    __extensionPath = f'{__base_dir}/release/Fingerprint.zip'

    def __init__(self, fingerprint):
        self._fingerprint = fingerprint

    def __loadManifest(self):
        with open(f'{self.__base_dir}/fingerprint/data/manifest.json', "r") as file:
            manifest_json = file.read()
        manifest_json = manifest_json
        return manifest_json

    def __loadPlatform(self):
        return platformSerialization(self._fingerprint['platform'])

    def __loadWebGL(self):
        return webGLSerialization(self._fingerprint['webGLHash'])

    def __loadCanvas(self):
        return canvasSerialization(self._fingerprint['CanvasHash'])

    def makeExtension(self):
        with zipfile.ZipFile(self.__extensionPath, 'w') as zp:
            zp.writestr("manifest.json", self.__loadManifest())
            zp.writestr("platform.js", self.__loadPlatform())
            zp.writestr("webGL.js", self.__loadWebGL())
            zp.writestr("canvas.js", self.__loadCanvas())
        return self.__extensionPath

