# imort de l'aglgorithm heapq permettant d'utiliser l'element list pour ajouter ou retirer des elements à une liste en la laissant toujours en ordre
import heapq
from heapq import heappop, heappush


def isLeaf(root):
    return root.left is None and root.right is None


# un noeud de l'arbre
class Node:
    def __init__(self, ch, freq, left=None, right=None):
        self.ch = ch
        self.freq = freq
        self.left = left
        self.right = right

    # On Override la finction  __lt__()  pour que le noeud marche avec priorité pour que la lettre avec la plus haute priorité ait la fréquence la moins élevée

    def __lt__(self, other):
        return self.freq < other.freq

#on traverse l'arbre de huffman et on stocke les codes de huffman pour chaque lettrre dans un dictionaire

def encode(root, str, huffman_code):
    if root is None:
        return

    # trouver la feuille d'un noeud
    if isLeaf(root):
        huffman_code[root.ch] = str if len(str) > 0 else '1'

    encode(root.left, str + '0', huffman_code)
    encode(root.right, str + '1', huffman_code)


#on parcours l'arbre et on décode le message encodé
def decode(root, index, str):
    if root is None:
        return index

    # trouver la feuille d'un noeud
    if isLeaf(root):
        print(root.ch, end='')
        return index

    index = index + 1
    root = root.left if str[index] == '0' else root.right
    return decode(root, index, str)

#On construit l'arbre et on décode le texte rentré en input
def buildHuffmanTree(text):
    # cas basique: la chaine est vide
    if len(text) == 0:
        return

    # on compte la fréquence d'apparution de chaque caractère et on le stocke dans un dictionnaire
    freq = {i: text.count(i) for i in set(text)}

    #  # on crée un chaine de priorité pour stocké nos différents noeuds de l'arbre
    pq = [Node(k, v) for k, v in freq.items()]
    heapq.heapify(pq)

    # on le fait tant qu'il y a plus d'un noeud dans la chaine
    while len(pq) != 1:
        # on enleve les 2 noeuds qui ont la plus haute priorité (la féquence la moins importante dans la chaine


        left = heappop(pq)
        right = heappop(pq)

        # On crée un noveau noeud avec ces 2 noeuds enfants avec la fréquence qui est égale à la somme des 2 noeuds

        #  on ajoute le nouveau noeud à la chaine de priorité

        total = left.freq + right.freq
        heappush(pq, Node(None, total, left, right))

    # root enregistre la racine de l'arbre de Huffman
    root = pq[0]

    # on parcours l'arbre de huffman et on la stock dans un dictionnaire

    huffmanCode = {}
    encode(root, "", huffmanCode)

    #la récureance de chaque lettre dans le message
    nbLetter=len(text.replace(" ", ""))

    print('le message original pèse ',nbLetter*8," octets")

    #on affiche les codes d'huffman
    print("les codes d'Huffman sont:", huffmanCode)
    print("Le message original est:", text)

    # on affiche le message encodé
    str = ""
    for c in text:
        str += huffmanCode.get(c)

    print("le message encodé est:", str)

    #on affiche en bytes le tockage de la taille compréssée
    byte=0
    for i in str:
        byte+=1

    print("la taille comprésse est de ",byte," octets")

    if isLeaf(root):
        # cas spéciaux: pour les input comme b, bbbb, bbbbbbb, etc.
        while root.freq > 0:
            print(root.ch, end='')
            root.freq = root.freq - 1
    else:
        # on traverse encore l'abre de huffman et cette fois in décode la chaine,
        index = -1
        while index < len(str) - 1:
            index = decode(root, index, str)


if __name__ == '__main__':
    text = input("rentrer votre chaine à encoder ici")
    buildHuffmanTree(text)
