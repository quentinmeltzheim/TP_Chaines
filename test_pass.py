# coding: utf-8 
import unittest
import password as pwd

class TestPassword(unittest.TestCase):

    def test_getNextNormal(self):
        self.assertEqual(pwd.getNext("bbcdd"), "bbcde")

    def test_getNextEndLine(self):
        self.assertEqual(pwd.getNext("fghhdzxx"), "fghhdzxy")

    def test_hasTwoPairs(self):
        self.assertEqual(pwd.hasTwoPairs("aabb"),True)

    def test_hasNoBadChar(self):
        self.assertEqual(pwd.hasNoBadChar("abced"),True)

    def test_hasSeries(self):
        self.assertEqual(pwd.hasSeries("abc"),True)

    def test_hasntTwoPairs(self):
        self.assertEqual(pwd.hasTwoPairs("ertyuioo"),False)

    def test_hasBadChar(self):
        self.assertEqual(pwd.hasNoBadChar("iol"),False)

    def test_hasntSeries(self):
        self.assertEqual(pwd.hasSeries("treg"),False)
# Permet d'exécuter les tests si ce fichier est exécuté
#unittest.main()