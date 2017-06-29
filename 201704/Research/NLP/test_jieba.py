#encoding:utf-8
import jieba.posseg as pseg
import jieba
#jieba.add_word("可口可乐")
jieba.add_word("可乐")
words = pseg.cut("可口可乐百事可乐对比")
for word, flag in words:
    print('%s %s' % (word, flag))
