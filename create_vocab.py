raw_vocab = open('/Users/lamhoangtung/Downloads/char_list.txt','r').read()
with open('./vocab.txt','w') as output:
    for each in raw_vocab:
        output.write(each+'\n')