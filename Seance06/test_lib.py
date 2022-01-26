"""Description.

Tests automatiques de lib.
"""
import pytest
from lib import Arbre, Assemblage, Feuille, parser, _supprime_blancs, _identifie_premiere_balise

def test_feuille_init():
    f = Feuille(nom="a")
    assert isinstance(f, Feuille)
    
def test_assemblage_init():
    b = Feuille(nom="b")
    c = Feuille(nom="c")
    a = Assemblage(nom="a", sous_arbres=[b, c])
    assert isinstance(a, Assemblage)
    
@pytest.mark.skip(reason="le subclass de générique n'est pas encore implémenté dans python.")
def test_arbre():
    b = Feuille(nom="b")
    c = Feuille(nom="c")
    assert isinstance(b, Arbre)
    a = Assemblage(nom="a", sous_arbres=[b, c]) 
    assert isinstance(a, Arbre)
    
def test_assemblage_repr():
    b = Feuille(nom="b")
    c = Feuille(nom="c")
    a = Assemblage(nom="a", sous_arbres=[b, c])
    assert repr(a) == "Assemblage(nom='a', sous_arbres=[Feuille(nom='b'), Feuille(nom='c')])"
    
    
def test_feuille_str():
    b = Feuille(nom="b")
    assert str(b) == "<b></b>"
    
def test_assemblage_str():
    b = Feuille(nom="b")
    c = Feuille(nom="c")
    a = Assemblage(nom="a", sous_arbres=[b, c])
    assert str(a) == "<a><b></b><c></c></a>"
    
def test_assemblage_eq():
    b = Feuille(nom="b")
    c = Feuille(nom="c")
    assert b != c
    a = Assemblage(nom="a", sous_arbres=[b, c])
    bb = Feuille(nom="b")
    cc = Feuille(nom="c")
    assert b == bb
    aa = Assemblage(nom="a", sous_arbres=[b, c])
    assert a == aa
        
        
def test_supprime_blancs():
    entree = """
a
    b
c d
"""
    assert _supprime_blancs(entree) == "abcd"
    
def test_identifie_premiere_balise():
    assert _identifie_premiere_balise("<a>") == "a"
    assert _identifie_premiere_balise("<A>") == "A"
    assert _identifie_premiere_balise("<balise>") == "balise"
    
def test_identifie_premiere_balise_echec():
    with pytest.raises(ValueError):
        _identifie_premiere_balise("abc>")
    with pytest.raises(ValueError):
        _identifie_premiere_balise("abcd")


@pytest.mark.skip(reason="Pas encore implémenté")
def test_parser():
    b = Feuille(nom="b")
    c = Feuille(nom="c")
    a = Assemblage(nom="a", sous_arbres=[b, c])
    code_a = str(a)
    assert parser(code_a) == a

@pytest.mark.skip(reason="Pas encore implémenté")
def test_parser_non_trivial():
    code = """
<a>
    <b>
    </b>
    <c>
        <d></d>
        <e></e>
    </c>
</a>
"""
    b = Feuille("b")
    d = Feuille("d")
    e = Feuille("e")
    c = Assemblage(nom="c", sous_arbres=[d, e])
    a = Assemblage(nom="a", sous_arbres=[b, c])
    assert parser(code) == a