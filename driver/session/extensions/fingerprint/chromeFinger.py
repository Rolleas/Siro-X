import zipfile
from pathlib import Path
from data.canvas import canvasSerialization
from data.platform import platformSerialization
from data.webGL import webGLSerialization


class Fingerprint:
    __platform = "Win32"
    __base_dir = Path(__file__).resolve().parent.parent
    __extensionPath = f'{__base_dir}/release/Fingerprint.zip'
    __WebGLHash = 0.1232321213
    __CanvasHash = {'r': 1, 'g': 1, 'b': 1, 'a': 1}

    @property
    def WebGLHash(self):
        return self.__WebGLHash

    @WebGLHash.setter
    def WebGLHash(self, value):
        if value == float:
            self.__WebGLHash = value

    @property
    def platform(self):
        return self.__platform

    @platform.setter
    def platform(self, value):
        if value == 'Win32' or value == 'MacIntel' or value == 'Linux':
            self.__platform = value

    def __loadManifest(self):
        with open(f'{self.__base_dir}/fingerprint/data/manifest.json', "r") as file:
            manifest_json = file.read()
        manifest_json = manifest_json
        return manifest_json

    def __loadPlatform(self):
        return platformSerialization(self.__platform)

    def __loadWebGL(self):
        return webGLSerialization(self.__WebGLHash)

    def __loadCanvas(self):
        return canvasSerialization(self.__CanvasHash)

    def makeExtension(self):
        with zipfile.ZipFile(self.__extensionPath, 'w') as zp:
            zp.writestr("manifest.json", self.__loadManifest())
            zp.writestr("platform.js", self.__loadPlatform())
            zp.writestr("webGL.js", self.__loadWebGL())
            zp.writestr("canvas.js", self.__loadCanvas())
        return self.__extensionPath

