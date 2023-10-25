from subprocess import run, Popen, PIPE

c = Popen(["cat"], stdin=PIPE, stdout=PIPE)
c.communicate(b'Hello World!\n')

run(["echo", "Hello", "World!"])

print("Sleeping")
# Popen(["bash", "-c", "sleep 5 && echo test"])
p = Popen(["sleep", "5"])
p.wait()
print("Slept")

