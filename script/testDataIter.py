import _pickle as pkl

from data_iterator import DataIterator
train_data = DataIterator('local_train_splitByUser', 'uid_voc.pkl', 'mid_voc.pkl', 'cat_voc.pkl', 1, 100, shuffle_each_epoch=False)
print(train_data.__next__())

# def unicode_to_utf8(d): return dict((key.encode("UTF-8"), value) for (key,value) in d.items())
#
#
# with open('uid_voc.pkl', 'rb') as f:
#   m=pkl.load(f)