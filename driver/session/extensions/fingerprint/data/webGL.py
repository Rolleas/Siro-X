def WebGLSerialization(WebGLHash):
    injectCode = """
            var inject = function () {
                var config = {
                    "random": {
                        "value": function () {
                            return %s;
                        },
                        "item": function (e) {
                            var rand = e.length * config.random.value();
                            return e[Math.floor(rand)];
                        },
                        "number": function (power) {
                            var tmp = [];
                            for (var i = 0; i < power.length; i++) {
                                tmp.push(Math.pow(2, power[i]));
                            }
                            /*  */
                            return config.random.item(tmp);
                        },
                        "int": function (power) {
                            var tmp = [];
                            for (var i = 0; i < power.length; i++) {
                                var n = Math.pow(2, power[i]);
                                tmp.push(new Int32Array([n, n]));
                            }
                            /*  */
                            return config.random.item(tmp);
                        },
                        "float": function (power) {
                            var tmp = [];
                            for (var i = 0; i < power.length; i++) {
                                var n = Math.pow(2, power[i]);
                                tmp.push(new Float32Array([1, n]));
                            }
                            /*  */
                            return config.random.item(tmp);
                        }
                    },
                    "spoof": {
                        "webgl": {
                            "buffer": function (target) {
                                var proto = target.prototype ? target.prototype : target.__proto__;
                                const bufferData = proto.bufferData;
                                Object.defineProperty(proto, "bufferData", {
                                    "value": function () {
                                        var index = Math.floor(config.random.value() * arguments[1].length);
                                        var noise = arguments[1][index] !== undefined ? 0.1 * config.random.value() * arguments[1][index] : 0;
                                        //
                                        arguments[1][index] = arguments[1][index] + noise;
                                        window.top.postMessage("webgl-fingerprint-defender-alert", '*');
                                        //
                                        return bufferData.apply(this, arguments);
            
                                    }
                                });
                            },
                            "parameter": function (target) {
                                var proto = target.prototype ? target.prototype : target.__proto__;
                                const getParameter = proto.getParameter;
            
                                Object.defineProperty(proto, "getParameter", {
                                    "value": function () {
                                        window.top.postMessage("webgl-fingerprint-defender-alert", '*');
                                        //
            
                                        if (arguments[0] === 3415) return 0;
                                        else if (arguments[0] === 3414) return 24;
                                        else if (arguments[0] === 36348) return 30;
                                        else if (arguments[0] === 7936) return "WebKit";
                                        else if (arguments[0] === 37445) return "Google Inc.";
                                        else if (arguments[0] === 7937) return "WebKit WebGL";
                                        else if (arguments[0] === 3379) return config.random.number([14, 15]);
                                        else if (arguments[0] === 36347) return config.random.number([12, 13]);
                                        else if (arguments[0] === 34076) return config.random.number([14, 15]);
                                        else if (arguments[0] === 34024) return config.random.number([14, 15]);
                                        else if (arguments[0] === 3386) return config.random.int([13, 14, 15]);
                                        else if (arguments[0] === 3413) return config.random.number([1, 2, 3, 4]);
                                        else if (arguments[0] === 3412) return config.random.number([1, 2, 3, 4]);
                                        else if (arguments[0] === 3411) return config.random.number([1, 2, 3, 4]);
                                        else if (arguments[0] === 3410) return config.random.number([1, 2, 3, 4]);
                                        else if (arguments[0] === 34047) return config.random.number([1, 2, 3, 4]);
                                        else if (arguments[0] === 34930) return config.random.number([1, 2, 3, 4]);
                                        else if (arguments[0] === 34921) return config.random.number([1, 2, 3, 4]);
                                        else if (arguments[0] === 35660) return config.random.number([1, 2, 3, 4]);
                                        else if (arguments[0] === 35661) return config.random.number([4, 5, 6, 7, 8]);
                                        else if (arguments[0] === 36349) return config.random.number([10, 11, 12, 13]);
                                        else if (arguments[0] === 33902) return config.random.float([0, 10, 11, 12, 13]);
                                        else if (arguments[0] === 33901) return config.random.float([0, 10, 11, 12, 13]);
                                        else if (arguments[0] === 37446) return config.random.item(["Intel(R) Iris(TM) Plus Graphics 655"]);
                                        else if (arguments[0] === 7938) return config.random.item(["Intel Inc."]);
                                        else if (arguments[0] === 35724) return config.random.item(["WebGL", "WebGL GLSL", "WebGL GLSL ES", "WebGL GLSL ES (OpenGL Chromium"]);
                                        //
                                        return getParameter.apply(this, arguments);
                                    }
                                });
                            }
                        }
                    }
                };
                //
                config.spoof.webgl.buffer(WebGLRenderingContext);
                config.spoof.webgl.buffer(WebGL2RenderingContext);
                config.spoof.webgl.parameter(WebGLRenderingContext);
                config.spoof.webgl.parameter(WebGL2RenderingContext);
                //
                document.documentElement.dataset.wgscriptallow = true;
            };
            
            var script_1 = document.createElement("script");
            script_1.textContent = "(" + inject + ")()";
            document.documentElement.appendChild(script_1);
            script_1.remove();
            
            if (document.documentElement.dataset.wgscriptallow !== "true") {
                var script_2 = document.createElement("script");
                script_2.textContent = `{
                const iframes = [...window.top.document.querySelectorAll("iframe[sandbox]")];
                for (var i = 0; i < iframes.length; i++) {
                  if (iframes[i].contentWindow) {
                    if (iframes[i].contentWindow.WebGLRenderingContext) {
                      iframes[i].contentWindow.WebGLRenderingContext.prototype.bufferData = WebGLRenderingContext.prototype.bufferData;
                      iframes[i].contentWindow.WebGLRenderingContext.prototype.getParameter = WebGLRenderingContext.prototype.getParameter;
                    }
                    if (iframes[i].contentWindow.WebGL2RenderingContext) {
                      iframes[i].contentWindow.WebGL2RenderingContext.prototype.bufferData = WebGL2RenderingContext.prototype.bufferData;
                      iframes[i].contentWindow.WebGL2RenderingContext.prototype.getParameter = WebGL2RenderingContext.prototype.getParameter;
                    }
                  }
                }
              }`;
                //
                window.top.document.documentElement.appendChild(script_2);
                script_2.remove();
            }
            """ % WebGLHash
    return injectCode
