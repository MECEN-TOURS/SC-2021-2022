"""Description.

Tests automatiques de lib.
"""
import pytest
from lib import (
    Arbre,
    parser,
    _supprime_blancs,
    _identifie_premiere_balise,
    _identifie_indice_balise_fermante,
    _extrait_interieur,
    _decoupe_code,
)


def test_arbre_feuille_init():
    a = Arbre(nom="a")
    assert isinstance(a, Arbre)


def test_arbre_init():
    b = Arbre(nom="b")
    c = Arbre(nom="c")
    a = Arbre(nom="a", sous_arbres=[b, c])
    assert isinstance(a, Arbre)


@pytest.fixture
def abc():
    b = Arbre(nom="b")
    c = Arbre(nom="c")
    a = Arbre(nom="a", sous_arbres=[b, c])
    return a, b, c


def test_arbre_repr(abc):
    a, b, c = abc
    assert (
        repr(a)
        == "Arbre(nom='a', sous_arbres=[Arbre(nom='b'), Arbre(nom='c')])"
    )


def test_arbre_str():
    b = Arbre(nom="b")
    assert str(b) == "<b></b>"


def test_arbre_str_branche(abc):
    a, b, c = abc
    assert str(a) == "<a><b></b><c></c></a>"


def test_arbre_eq(abc):
    a, b, c = abc
    assert b != c
    bb = Arbre(nom="b")
    cc = Arbre(nom="c")
    assert b == bb
    aa = Arbre(nom="a", sous_arbres=[bb, cc])
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


def test_identifie_balise_fermante():
    assert _identifie_indice_balise_fermante(balise="a", code="<a></a>") == 3
    assert _identifie_indice_balise_fermante(balise="a", code="<b><a></a></b>") == 6


def test_identifie_balise_fermante_echec():
    with pytest.raises(ValueError):
        _identifie_indice_balise_fermante(balise="b", code="<a></a>")


def test_extrait_interieur():
    entree = "<a><b><c></c></b><d></d></a>"
    assert _extrait_interieur(code=entree) == "<b><c></c></b><d></d>"


def test_decoupe_code():
    entree = "<b><c></c></b><d></d>"
    assert _decoupe_code(code=entree) == ["<b><c></c></b>", "<d></d>"]


def test_parser(abc):
    a, b, c = abc
    code_a = str(a)
    assert parser(code_a) == a


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
    b = Arbre("b")
    d = Arbre("d")
    e = Arbre("e")
    c = Arbre(nom="c", sous_arbres=[d, e])
    a = Arbre(nom="a", sous_arbres=[b, c])
    assert parser(code) == a
