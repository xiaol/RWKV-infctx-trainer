from  rwkv.rwkv_tokenizer import TRIE_TOKENIZER

def test():
    old_vocabs_tokenizer = TRIE_TOKENIZER('./rwkv_vocab_v20230424.txt')
    new_vocabs_tokenizer = TRIE_TOKENIZER('./rwkv_vocab_v20230424_new.txt')

    def token_it(tokenizer):

        eos_old = tokenizer.encode("</s>")
        bos_old = tokenizer.encode("<s>")
        print(*eos_old)
        print(*bos_old)

        eos = tokenizer.decode(eos_old)
        bos = tokenizer.decode(bos_old)
        print(*eos, sep='')
        print(*bos, sep='')
        
        

    token_it(old_vocabs_tokenizer)
    token_it(new_vocabs_tokenizer)


def test2():
    old_vocabs_tokenizer = TRIE_TOKENIZER('./rwkv_vocab_v20230424.txt')
    
    eos = old_vocabs_tokenizer.decode([65530])
    bos = old_vocabs_tokenizer.decode([65531])

    print(*eos, sep='')
    print(*bos, sep='')
        

if __name__ == '__main__':
    #translate_with_rwkv()
    #res = keywords(r"标题：鼓风机\n摘要：本发明提供一种降低噪音的鼓风机。根据本发明的一种方式，提供了一种鼓风机。所述鼓风机具备内置离心风扇的鼓风机主体。鼓风机主体构成为能够根据离心风扇的旋转而从其两侧面吸引空气。离心风扇包括具有旋转中心的支承板，以及分别设置在支承板的第一面及第二面的多个叶片。第一面的多个叶片中的至少一部分的位置与第二面的多个叶片中的至少一部分的位置在周向上偏移，及/或第一面的多个叶片的数量与第二面的多个叶片的数量不同。")
    test2()
    #print(res)