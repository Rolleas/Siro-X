def platformSerialization(platform, deviceMemory, hardwareConcurrency):
    injectCode = """
    var codeToInject = 'Object.defineProperty(navigator,"platform", { \
                    get: function () { return "%s"; }, \
                    set: function (a) {} \
                    });';
                    
    var script = document.createElement('script');
    script.appendChild(document.createTextNode(codeToInject));
    (document.head || document.documentElement).appendChild(script);
    script.parentNode.removeChild(script);
    
    var codeToInject2 = 'Object.defineProperty(navigator,"deviceMemory", { \
                    get: function () { return "%s"; }, \
                    set: function (a) {} \
                    });';
                    
    var script = document.createElement('script');
    script.appendChild(document.createTextNode(codeToInject2));
    (document.head || document.documentElement).appendChild(script);
    script.parentNode.removeChild(script);
    
    var codeToInject3 = 'Object.defineProperty(navigator,"hardwareConcurrency", { \
                    get: function () { return "%s"; }, \
                    set: function (a) {} \
                    });';
                    
    var script = document.createElement('script');
    script.appendChild(document.createTextNode(codeToInject3));
    (document.head || document.documentElement).appendChild(script);
    script.parentNode.removeChild(script);
    
    """ % platform, deviceMemory, hardwareConcurrency
    return injectCode
