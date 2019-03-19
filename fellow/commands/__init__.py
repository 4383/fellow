from fellow.lib import plugins


class Interpreter:
    def __init__(self):
        commands = plugins.load()
        module = __import__("fellow.lib.modules", fromlist=commands)
        cmds = []
        for cmd in commands:
            mod = getattr(module, cmd)
            instance = getattr(mod, cmd.capitalize())()
            cmds.append(
                {
                    cmd: {
                        "object": instance,
                        "subcmds": [
                            method
                            for method in dir(instance)
                            if not method.startswith("_")
                        ],
                    }
                }
            )
        print(cmds)
