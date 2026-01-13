from ndspy import rom, codeCompression as comp

# Change to whatever .nds file you want to test
r = rom.NintendoDSRom.fromFile("pokemon.nds")

# Decompress arm9 with ndspy
decompressed_nds = comp.decompress(r.arm9)
open("arm9_ndspy_decompressed.bin","wb").write(decompressed_nds)

# Find shiny offset rate pattern in decompressed arm9
pattern = bytes.fromhex("082801D201")  # adjust pattern as needed
def find_all(data,p):
    i=0; out=[]
    while True:
        i=data.find(p,i)
        if i==-1: break
        out.append(i); i+=1
    return out

# Print results
print("search pattern:", pattern.hex())
print("ndspy matches:", [hex(x) for x in find_all(decompressed_nds,pattern)])
