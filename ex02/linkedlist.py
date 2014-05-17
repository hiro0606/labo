# -*- coding: utf-8 -*-
'''
参考：http://ja.wikipedia.org/wiki/連結リスト

課題1
    __reversed__()とMyReverseIterator以外を実装し連結リストを完成させよ

課題2
    先週実装したqsortで連結リストを並び替えられるようにせよ

課題3
        MyLinkedList.__reversed__()
        MyReverseIterator
    を実装し、両方向リストを完成させよ。逆方向のリンクはNode.prevという名前
    のインスタンス変数で保持すること。
'''

from collections import Iterator, Sequence, MutableSequence,Iterable


class MyLinkedList(object): # Sequence):  # MutableSequence):

    def __init__(self):
        'コンストラクタ'
        self.head = Node(None)
        #self.position = -1

    def __contains__(self, value):
        '''inステートメントで呼ばれる特殊メソッド

        collections.Sequence基底クラスのMixinメソッド

        inステートメントで呼ばれる。value in self の結果をTrueかFalseで返す

            >>> l = MyLinkedList()
            >>> l.append(1)
            >>> 1 in l  # l.__contains__(1) に等しい
            True
            >>> 2 in l
            False

        '''
        if self.count(value) != 0:
            return True
        else:
            return False

    def __iter__(self):
        '''iter関数で呼ばれる特殊メソッド

        collections.Sequence基底クラスのMixinメソッド

        イテレータデザインパターンにおけるイテレータオブジェクトを返す。Python
        においては、主にfor文で用いられる。

            for a in b:
                do(a)

        は次のコードと等しい。

            iterator = iter(b)  # = b.__iter__()
            try:
                while True:
                    a = next(iterator)  # = iterator.next()
                    do(a)
            except StopIteration:
                pass

        (余談) Python3からはnext組み込み関数で呼ばれるのが、nextメソッドから
        __next__特殊メソッドに変更されました。

            >>> l = MyLinkedList()
            >>> l.append(1)
            >>> iterator = iter(l)
            >>> isinstance(iterator, MyIterator)
            True
            >>> next(iterator)
            1

        iteratorオブジェクトは最後まできたらStopIteration例外を発生させなければ
        ならない。

            >>> item = next(iterator)
            Traceback (most recent call last):
                ...
            StopIteration

        __iter__特殊メソッドを実装することでfor文で使うことができるようになる。

            >>> l.append(2)
            >>> for i in l:
            ...     print i
            ...
            1
            2

        '''
        """
        for i in range(len(self)):
            yield self[i]
        """
        def generator(linkedlist):
            for i in range(len(linkedlist)):
                yield linkedlist[i]
        my_iterator = MyIterator(generator(self))
        return my_iterator


    def __len__(self):
        '''len関数で呼ばれる特殊メソッド

            >>> l = MyLinkedList()
            >>> len(l)
            0
            >>> l.append(1)
            >>> len(l)
            1
            >>> l.append(2)
            >>> len(l)
            2

        '''
        length = 0
        current_node = self.head
        while current_node.next != None:
            length += 1
            current_node = current_node.next
        return length


    def __getitem__(self, key):
        '''インデックス記法で呼ばれる特殊メソッド

        collections.Sequence基底クラスの抽象メソッド

        配列のようなインデックス記法を用いた場合に呼び出され、``key''番目の要素
        の値を返す。

            >>> l = MyLinkedList()
            >>> l.append(1)
            >>> l[0]    # l.__getitem__(0)
            1

        設定されていないインデックスにアクセスされた場合はIndexError例外を発生
        させなければならない。

            >>> l[2]
            Traceback (most recent call last):
                ...
            IndexError

        ``key''が数字以外だった場合TypeError例外を発生させなければならない

            >>> l['string']
            Traceback (most recent call last):
                ...
            TypeError

        ``key''の値は-len(self) <= key < len(self)でなければならず、範囲外の
        場合はIndexError例外を発生させなければならない。

            >>> l.append(2)
            >>> l[-2]
            1
            >>> l[2]
            Traceback (most recent call last):
                ...
            IndexError
            >>> l[-3]
            Traceback (most recent call last):
                ...
            IndexError

        '''
        if isinstance(key,int):
            current_node = self.head
            if -len(self) <= key < len(self):#index範囲内にあるとき
                if -len(self) <= key < 0:
                    count = key + len(self)
                else:
                    count = key
                while count >= 0:
                    current_node = current_node.next
                    count -= 1
                return current_node.value
            else:
                raise IndexError()
        else:
            raise TypeError()

    def __setitem__(self, key, value):
        '''インデックス記法を用いた代入文で呼ばれる特殊メソッド

        collections.MutableSequence基底クラスの抽象メソッド

        ``key''番目の値を``value''に置き換える。

            >>> l = MyLinkedList()
            >>> l.append(1)  # [1]
            >>> l[0] = 2     # [2]
            >>> l[0]
            2

        設定されていないインデックスに対して代入を行おうとした場合はIndexError
        例外を発生させなければならない。

            >>> l[1] = 2
            Traceback (most recent call last):
                ...
            IndexError

        ``key''が数字以外だった場合TypeError例外を発生させなければならない

            >>> l['string'] = 2
            Traceback (most recent call last):
                ...
            TypeError

        ``key''の値は-len(self) <= key < len(self)でなければならず、範囲外の
        場合はIndexError例外を発生させなければならない。

            >>> l.append(2) # [2, 2]
            >>> l[-2] = 3   # [3, 2]
            >>> l[0]
            3
            >>> l[2]
            Traceback (most recent call last):
                ...
            IndexError
            >>> l[-3]
            Traceback (most recent call last):
                ...
            IndexError

        '''
        if isinstance(key,int):
            if -len(self) <= key < len(self):
                ###keyが負のとき###
                if -len(self) <= key < 0:
                    count = len(self) + key
                else:
                    count = key
                current_node = self.head
                while count >= 0:
                    current_node = current_node.next
                    count -= 1
                current_node.value = value
            else: raise IndexError()
        else: raise TypeError()


    def __delitem__(self, key):
        '''インデックス記法を用いて削除を行う

        collections.MutableSequence基底クラスの抽象メソッド

        delステートメントで``key''番目の値を削除する

            >>> l = MyLinkedList()
            >>> l.append(1)
            >>> l.append(2)
            >>> l[0]
            1
            >>> del l[0]
            >>> l[0]
            2

        設定されていないインデックスの削除を行おうとした場合はIndexErrorを発生
        させなければならない。

            >>> del l[1]
            Traceback (most recent call last):
                ...
            IndexError

        ``key''が数字以外だった場合TypeError例外を発生させなければならない

            >>> del l['string']
            Traceback (most recent call last):
                ...
            TypeError

        ``key''の値は-len(self) <= key < len(self)でなければならず、範囲外の
        場合はIndexError例外を発生させなければならない。

            >>> del l[-1]
            >>> l[0]
            Traceback (most recent call last):
                ...
            IndexError

        '''
        if isinstance(key,int):
            if -len(self) <= key < len(self):
                ###keyが負のとき###
                if -len(self) <= key < 0:
                    count = len(self) + key
                else:
                    count = key
                current_node = self.head
                ###key番目のノードへのlinkをkey+1番目のノードへ切り替える###
                while count >= 0:
                    current_node = current_node.next
                    count -= 1
                current_node.prev.next = current_node.next
                #k番目のノードが最後のノードでなければ
                if current_node.next != None:
                    current_node.next.prev = current_node.prev

            else: raise IndexError()
        else: raise TypeError()

    def __iadd__(self, value):
        '''+=オペランドで呼ばれる特殊メソッド

        collections.MutableSequence基底クラスのMixinメソッド

        戻り値が代入される

            >>> l = MyLinkedList()
            >>> l += 1
            >>> l[0]
            1
            >>> l += 2
            >>> l[1]
            2

        '''
        self.append(value)
        return self





    def __reversed__(self):
        '''reversed組み込み関数で呼ばれる特殊メソッド

        collections.Sequence基底クラスのMixinメソッド

        逆方向にたどるためのイテレータオブジェクトを返す。

            >>> l = MyLinkedList()
            >>> l.append(1)
            >>> l.append(2)
            >>> iterator = reversed(l)
            >>> isinstance(iterator, MyReverseIterator)
            True
            >>> next(iterator)
            2
            >>> next(iterator)
            1

        最後まできたらStopIteration例外を発生させなければならない

            >>> next(iterator)
            Traceback (most recent call last):
                ...
            StopIteration

        for文で用いることも可能

            >>> for i in reversed(l):
            ...     print i
            ...
            2
            1

        '''
        def generator(linkedlist):
            linkedlist.reverse()
            for i in range(len(linkedlist)):
                yield linkedlist[i]
            linkedlist.reverse()
        iterator = generator(self)
        mri = MyReverseIterator(iterator)
        return mri

        """
        self.reverse()
        for i in range(len(self)):
            yield self[i]
        #linkedlistの順番を元に戻しておく
        self.reverse()
        """

    def append(self, value):
        '''リストの末尾に``value''を加える

        collections.MutableSequence基底クラスのMixinメソッド

            >>> l = MyLinkedList()
            >>> l.append(1)
            >>> l.append(2)

        '''
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        last_node = Node(value)
        last_node.prev = current_node
        current_node.next = last_node

    def pop(self):
        '''リストの末尾から値を一つ取り出す

        collections.MutableSequence基底クラスのMixinメソッド

            >>> l = MyLinkedList()
            >>> l.append(1)
            >>> l.pop()
            1

        空のリストに対して読んだ場合、IndexError例外を発生させなければならない

            >>> l.pop()
            Traceback (most recent call last):
                ...
            IndexError

        '''
        if self.head.next != None:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            current_node.prev.next = None #後ろから二番目のノードを最後のノードにする
            return current_node.value
        else: raise IndexError()


    def reverse(self):
        '''自分自身の順番を逆にする

        collections.MutableSequence基底クラスのMixinメソッド
        破壊的メソッドであることに注意。また、このメソッド自体は値を返さない。

            >>> l = MyLinkedList()
            >>> l.append(1)
            >>> l.append(2)
            >>> l.reverse()
            >>> l.pop()
            1
            >>> l.pop()
            2

        '''
        """
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            current_node.prev,current_node.prev.next = current_node.prev.next,current_node.prev

        self.head.next = current_node
        current_node.next = current_node.prev
        current_node.prev = self.head
        """

        #ノードがあれば
        if self.head.next != None:
            current_node = self.head
            while current_node.next != None:
                #一つ前のノードを保存しておく
                previous_node = current_node.prev
                #注目ノードのnextとprevを入れ替える
                current_node.prev = current_node.next
                current_node.next = previous_node
                #次のノードへ
                current_node = current_node.prev
            #入れ替え後の末尾ノードとself.headのlinkを切る
            self.head.prev.next = None

            self.head.next = current_node
            current_node.next = current_node.prev
            current_node.prev = self.head
            

            


    def index(self, value):
        '''``value''が最初に現れるインデックスを返す

        collections.Sequence基底クラスのMixinメソッド

            >>> l = MyLinkedList()
            >>> l.append(1)
            >>> l.append(2)
            >>> l.append(1)
            >>> l.index(1)
            0
            >>> l.index(2)
            1

        ``value''が存在しない場合はValueError例外を発生させなければならない。

            >>> l.index(3)
            Traceback (most recent call last):
                ...
            ValueError

        '''
        index = -1
        current_node = self.head
        while current_node != None:
            if current_node.value == value:
               return index

            index += 1
            current_node = current_node.next
        raise ValueError

    def insert(self, key, value):
        '''リストへの挿入

        collections.MutableSequence基底クラスの抽象メソッド

        ``key''番目に``value''を挿入する。

            >>> l = MyLinkedList()
            >>> l.append(1)       # [1]
            >>> l.insert(0, 2)    # [2, 1]
            >>> l.insert(1, 3)    # [2, 3, 1]
            >>> l.insert(-1, 4)   # [2, 3, 4, 1]
            >>> l.insert(-3, 6)   # [2, 6, 3, 4, 1]
            >>> l.insert(-5, 5)   # [5, 2, 6, 3, 4, 1]
            >>> l.pop()
            1
            >>> l.pop()
            4
            >>> l.pop()
            3

        ``key``が大きすぎるもしくは小さすぎる場合は端に挿入される。例外は発生
        しない。

            >>> l.append(1)       # [5, 2, 6, 1]
            >>> l.insert(100, 2)  # [5, 2, 6, 1, 2]
            >>> l.pop()
            2
            >>> l.insert(-100, 0) # [0, 5, 2, 6, 1]
            >>> l.pop()
            1
            >>> l.pop()
            6
            >>> l.pop()
            2
            >>> l.pop()
            5
            >>> l.pop()
            0

        '''

        if isinstance(key,int):
            #keyがlist長以上でなければ
            if key < len(self):
                if -len(self) <= key < 0:
                    count = key + len(self)
                elif 0 <= key < len(self):
                    count = key
                #keyが小さすぎたとき
                else:
                    count = 0
    
                current_node = self.head
                while count >= 0:
                    current_node = current_node.next
                    count -= 1
    
                new_node = Node(value)
                #keyがlen(self)以上でなければ
                if current_node != None:
                    #key-1番目のノードとnew_nodwをつなぐ
                    new_node.prev = current_node.prev
                    current_node.prev.next = new_node
                    #key番目のノードとnew_nodeをつなぐ
                    new_node.next = current_node
                    current_node.prev = new_node
            #keyがlist長以上であれば
            else:
                current_node = self.head
                while current_node.next != None:
                    current_node = current_node.next
                new_node = Node(value)
                current_node.next = new_node
                new_node.prev = current_node
        else: raise TypeError()

    def count(self, value):
        '''要素の数え上げ

        collections.Sequence基底クラスのMixinメソッド

        ``value''と値が等しいオブジェクトが含まれる数を返す。

            >>> l = MyLinkedList()
            >>> l.append(1)
            >>> l.append(2)
            >>> l.append(1)
            >>> l.count(1)
            2
            >>> l.count(3)
            0

        同一のオブジェクトである必要はない

            >>> 1 is 1.0  # ヒント1
            False
            >>> 1 == 1.0  # ヒント2
            True
            >>> l.count(1.0)
            2

        '''
        current_node = self.head
        count = 0
        while current_node.next != None:
            current_node = current_node.next
            if current_node.value == value:
                count += 1
        return count

    def remove(self, value):
        '''要素の削除

        collections.MutableSequence基底クラスのMixinメソッド

        ``value''と値が等しいオブジェクトの内、最もインデックスの小さいものを
        削除する

            >>> l = MyLinkedList()
            >>> l.append(1)
            >>> l.append(2)
            >>> l.append(1)
            >>> l.append(2)
            >>> l.remove(2)
            >>> l.pop()
            2
            >>> l.pop()
            1
            >>> l.pop()
            1
            >>> l.pop()
            Traceback (most recent call last):
                ...
            IndexError

        存在しない値が指定された場合はValueError例外を発生させなければならない

            >>> l.remove(2)
            Traceback (most recent call last):
                ...
            ValueError

        '''
        exist_flag = False
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            if current_node.value == value:
                #末尾のノードのvalueと一致した場合
                if current_node.next == None:
                    current_node.prev.next = None
                    exist_flag = True
                    break
                else:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                    exist_flag = True
                    break
        if exist_flag is False:
            raise ValueError


    def extend(self, seq):
        '''要素の拡張

        collections.MutableSequence基底クラスのMixinメソッド

        ``seq''を末尾に追加する。``seq''はiterableなオブジェクトでなければなら
        ない。

            >>> l = MyLinkedList()
            >>> l.extend([1,2,3])
            >>> l.pop()
            3
            >>> l.pop()
            2
            >>> l.pop()
            1

        iterableかどうかは次のようにして知ることができる

            >>> from collections import Iterable
            >>> isinstance([], Iterable)
            True
            >>> isinstance((), Iterable)
            True
            >>> isinstance({}, Iterable)
            True
            >>> isinstance(1, Iterable)
            False
            >>> isinstance('', Iterable)  # 文字列はiterable
            True
            >>> 'string'[1]
            't'

        '''
        if isinstance(seq,Iterable):
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            for i in seq:
                new_node = Node(i)
                current_node.next = new_node
                new_node.prev = current_node
                current_node = new_node
        else: raise TypeError()


class MyIterator(Iterator):
    '''MyLinkedListインスタンスに対するイテレータ'''

    def __init__(self,Iterator):
        self.iterator = Iterator

    def next(self):
        '''イテレータプロトコル

        collections.Iterator基底クラスの抽象メソッド

        最後まできた場合はStopIteration例外を発生させなければならない。
        詳しくはMyLinkedList.__iter__特殊メソッドのコメント参照
        '''
        return self.iterator.next()


    # python3から__next__特殊メソッドに変更された
    __next__ = next


class MyReverseIterator(Iterator):
    '''MyLinkedListインスタンスに対する逆方向のイテレータ'''

    def __init__(self,Iterator):
        self.iterator = Iterator

    def next(self):
        '''イテレータプロトコル

        collections.Iterator基底クラスの抽象メソッド

        最後まできた場合はStopIteration例外を発生させなければならない。
        詳しくはMyLinkedList.__reversed__特殊メソッドのコメント参照
        '''
        return self.iterator.next()

    # python3から__next__特殊メソッドに変更された
    __next__ = next


class Node(object):
    '''ノード'''
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        'printステートメントなどで呼ばれる'
        return repr(self.value)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
