import os
k = 1
file_name = "file" + str(k) + ".txt"
i = 0
while True:
    with open(file_name, "a") as f:
        f.write("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
        i += 1
        if i >= 1000:
            file_size = os.path.getsize(file_name)
            if file_size >= 1000000000:
                k += 1
                file_name = "file" + str(k) + ".txt"
            i = 0
