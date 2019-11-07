import r2pipe
import os

if __name__ == "__main__":
    root_dir = 'data/ELF-benign'
    output_dir = "method/1/benign"
    try:
        os.mkdir(output_dir)
    except:
        pass
    for dname in os.listdir(root_dir):
        print(dname, "processing...")
        # try:
        #     os.mkdir(os.path.join(output_dir, dname))
        # except:
        #     pass
        path = os.path.join(root_dir, dname)
        for fname in os.listdir(path):
            print(fname, "..............")
            file_path = os.path.join(path, fname)
            oFile = os.path.join(output_dir, fname + ".dot")
            r2 = r2pipe.open(file_path)
            r2.cmd('aaa')
            graph = r2.cmd("agC")
            # print(graph)
            with open(oFile, mode="w") as f:
                f.write(graph)
            # break
        # break