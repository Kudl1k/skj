#!/usr/bin/env python
# coding: utf-8

# ### Úkol 1 (20 bodů)

# In[ ]:


"""
Naimplementujte třídu Knihovna.
Knihovna obsahuje databázi knih, ke každé knize si udržuje počet dostupných kopií.

Metody, které máte naimplementovat a ukázka použití:
    knihovna = Knihovna()

    # Přidá knihu do knihovny
    knihovna.pridej_knihu("Harry Potter")
    knihovna.pridej_knihu("Harry Potter")
    knihovna.pridej_knihu("Lord of the Rings")
    knihovna.pridej_knihu("Artemis Fowl")


    # Pokud je v knihovně alespoň jedna kopie dané knihy, tak se jedna kopie z knihovny odebere a funkce vrátí True.
    # Pokud v knihovně daná kniha není, funkce vrátí False.
    knihovna.vypujc_knihu("Lord of the Rings") # True

    # Vrátí celkový počet všech kopií všech knih, které jsou v knihovně.
    knihovna.vrat_pocet_kopii() # 3

    # Vrátí knihu, která má v knihovně nejvíce kopií.
    # Pokud je takových knih více, vraťte libovolnou z nich.
    # Pokud v knihovně žádná kniha není, vraťte None.
    knihovna.vrat_nejcetnejsi_knihu() # "Harry Potter"
"""
# Zde piste kod
raise NotImplementedError()


# In[ ]:


# zde můžete testovat, jak třída funguje


# In[ ]:


knihovna = Knihovna()
assert knihovna.vypujc_knihu("Gang of Four") == False
assert knihovna.vrat_pocet_kopii() == 0

knihovna.pridej_knihu("Gang of Four")
knihovna.pridej_knihu("Compilers")
assert knihovna.vrat_pocet_kopii() == 2

assert knihovna.vypujc_knihu("Gang of Four") == True
assert knihovna.vypujc_knihu("Gang of Four") == False
assert knihovna.vrat_pocet_kopii() == 1
assert knihovna.vrat_nejcetnejsi_knihu() == "Compilers"

knihovna.pridej_knihu("Compilers")
assert knihovna.vrat_pocet_kopii() == 2

assert knihovna.vypujc_knihu("Compilers") == True
assert knihovna.vypujc_knihu("Compilers") == True
assert knihovna.vypujc_knihu("Compilers") == False
assert knihovna.vrat_pocet_kopii() == 0

knihovna.pridej_knihu("Computer architecture")
knihovna.pridej_knihu("Python for beginners")
knihovna.pridej_knihu("Operating systems")
knihovna.pridej_knihu("Python for beginners")
knihovna.pridej_knihu("Computer architecture")
knihovna.pridej_knihu("Python for beginners")
assert knihovna.vrat_nejcetnejsi_knihu() == "Python for beginners"


# ### Úkol 2 (15 bodů)

# In[ ]:


"""
Otevřete CSV soubor na zadané cestě a načtěte z něj údaje.
Spočítejte průměrný počet bodů pro každý předmět v souboru a vraťte jej z funkce jako slovník
{předmět: průměrný počet bodů}.

CSV soubor má následující formát:
jmeno,predmet,body

Příklad:
Jan Novák,SPJA,16
Anna Melíšková,UDBS,8
Karel Pěchota,UDBS,30
Jaroslav Němec,SPJA,6

Ze souboru výše by měl vyjít slovník
{
 "SPJA": 11,
 "UDBS": 19
}
"""
# Zde piste kod
raise NotImplementedError()


# In[ ]:


# zde můžete testovat, co funkce vrací


# In[ ]:


assert prumery("data.csv") == {
    "SPJA": 71,
    "UDBS": 44,
    "DIM": 69
}


# ### Úkol 3 (5 bodů)

# In[ ]:


"""
Vraťte True, pokud je zadaný řetězec palindrom (čte se stejně zepředu i pozpátku).

Příklad:
je_palindrom('a') # True
je_palindrom('aaa') # True
je_palindrom('aba') # True
je_palindrom('abc') # False
"""
# Zde piste kod
raise NotImplementedError()


# In[ ]:


# zde můžete testovat, co funkce vrací


# In[ ]:


assert je_palindrom('')
assert je_palindrom('a')
assert je_palindrom('aa')
assert je_palindrom('aaa')
assert je_palindrom('aba')
assert not je_palindrom('abc')
assert not je_palindrom('abcd')
assert not je_palindrom('palindrom')