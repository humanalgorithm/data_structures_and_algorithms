
test = "testing,this,string,of,otherword,stuff"

test2 = test.split(',')


print "test2 is " + str(test2)
print "test2 at index 2 is " + test2[1]


longest = "a"
for z in range (0, len(test2)):
    if len(test2[z]) > len(longest):
        print "found something longer at index x="  + str(z) + " " + str(test2[z]) + " length is " + str(len(test2[z]))
        longest = test2[z]

print longest


for x in range (0,10):
    print str(x)


    #what is x? 0,1,2,3...
    #what is test2? ['word', 'otherword', 'words'...]
    #what is len? len("five") = 4

    #     test2[x]  --> when x =1 value will be 'otherword'
    #   len(test2[x]) --> when x = 1 len of 'otherword' which equals 9
