# coding: utf-8 
import unittest
import password as pwd

class TestPassword(unittest.TestCase):

    def test_getNextNormal(self):
        self.assertEqual(pwd.getNext("abcd"), "abce")

    def test_getNextEndLine(self):
        self.assertEqual(pwd.getNext("abhz"), "abia")

    def test_getNextZ(self):
        self.assertEqual(pwd.getNext("zzzz"), "Erreur lors de la conversion de zzz")

# Permet d'exécuter les tests si ce fichier est exécuté
#unittest.main()