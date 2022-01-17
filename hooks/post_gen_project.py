from subprocess import Popen, PIPE


def exec(script):
    p = Popen(args=[script], stdout=PIPE)
    (output, err) = p.communicate()
    p.wait()
    return output.decode("UTF-8").strip().replace("nil", "").replace('"', "")


def bash(cmd):
    p = Popen(args=["/usr/bin/env", "bash", "-c", cmd], stdout=PIPE)
    (output, err) = p.communicate()
    p.wait()
    return output.decode("UTF-8").strip().replace("nil", "").replace('"', "")


prefix = bash("which s")
print(prefix)
# add runner to project
# secretsviakvproj
