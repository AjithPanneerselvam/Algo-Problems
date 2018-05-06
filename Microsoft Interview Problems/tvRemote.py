"""
Given a TV remote: The keypad numbered from 0 – 9 is also mapped to alphabets (a-z) 
[i.e. 1-a, b, c; 2-d, e, f; so on]. Also given is a long list of channel names. 
User will provide an input i.e. digit string – Task is to display all channel names 
that start with the different string combinations that are produced through user input. 
[i.e. Input ’12’ will correspond to combinations ‘ad’ ‘ae’ ‘af’ ‘bd’ ‘be’ ‘bf’ ‘cd’ ‘ce’ ‘cf’. 
Hence display all channel names that start with these combinations].
"""

keypad = {
        '1' : "abc",
        '2' : "def",
        '3' : "ghi",
        '4' : "jkl",
        '5' : "mno",
        '6' : "pqr",
        '7' : "stu",
        '8' : "vwx",
        '9' : "yz" 
    }
    

def printAllChannelNames(digitString, length, index, channelName):
    if(length == index):
        print(channelName)
        return
    
    for i in range(len(keypad[digitString[index]])):
        channelName += keypad[digitString[index]][i]
        printAllChannelNames(digitString, length, index + 1, channelName)
        channelName = channelName[:len(channelName) - 1]


digitString = "12"
printAllChannelNames(digitString, len(digitString), 0, "")


