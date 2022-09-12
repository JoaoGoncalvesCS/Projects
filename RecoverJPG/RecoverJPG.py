#Open drive as raw bites
drive = "\\\\.\\G:"
fileD = open(drive, "rb")

#Size of bytes to read
size = 512

#Read "size" bytes
byte = fileD.read(size)

#Offset location
offs = 0

#Recovery Mode
drec = False

#Recovery file ID
rcvd = 0

while byte:
    found = byte.find(b'\xff\xd8\xff\xe0\x00\x10\x4a\x46')
    if found >= 0:
        drec = True
        print('==== Found JPG at location: ' + str(hex(found+(size*offs))) + '====')
        
        #Now lets create recovered file and search for ending signature
        fileN = open('1\\' + str(rcvd) + '.jpg', "wb")
        fileN.write(byte[found:])
        while drec:
            byte = fileD.read(size)
            bfind = byte.find(b'\xff\xd9')
            if bfind >= 0:
                fileN.write(byte[:bfind+2])
                fileD.seek((offs+1)*size)
                print('==== Wrote JPG to location: ' + str(rcvd) + '.jpg ====\n')
                drec = False
                rcvd += 1
                fileN.close()
            else:
                fileN.write(byte)
    byte = fileD.read(size)
    offs += 1
fileD.close()