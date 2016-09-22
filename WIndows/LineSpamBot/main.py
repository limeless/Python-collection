# -*- coding: utf-8 -*-
import line
import time

def main():

    try:
        client = line.LineClient("account", "password", com_name='Spamming System Loaded.')
        #client = LineClient(authToken="AUTHTOKEN")
    except:
        print "Login Failed"

    print "Logged in."
    profile = client.profile
    print "Currently Profile Name Is %s" % profile
    
    contact_list = []
    contact_list = client.contacts
    print "Numbers of Friends : %s" % len(contact_list)
    group_list = []
    group_list = client.groups
    print "Numbers of Groups : %s" % len(group_list)
    
    
    ## Start mashing the message.
    pend = 0
    pend_g = 0
    file = open('post.txt', 'r')
    txt = file.readline():
        
    for x in contact_list:
        pending = client.contacts[pend]
        pending.sendMessage('%s' % txt)
        print "%s to %s : %s" % profile, client.contacts[pend], txt
        x = x + 1
        #Prending LINE BAN IP
        time.sleep(0.5)
        
    for y in group_list:
        pending_g = client.groups[pend_g]
        pending_g.sendMessage('%s' % txt)
        print "%s to %s : %s" % profile, client.groups[pend_g], txt
        y = y + 1
        #Prending LINE BAN IP
        time.sleep(0.5)
        
    print "done."
    
    
if __name__ == '__main__':
    main()