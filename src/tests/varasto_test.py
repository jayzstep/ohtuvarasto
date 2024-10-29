import unittest

from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivinen_tilavuus_palauttaa_nollan(self):
        mahdoton_varasto = Varasto(-10)

        self.assertEqual(mahdoton_varasto.tilavuus, 0)

    def test_negatiivinen_alkusaldo_nollautuu(self):
        mahdoton_varasto = Varasto(10, -10)

        self.assertEqual(mahdoton_varasto.saldo, 0)

    def test_ylimaarainen_saldo_haviaa(self):
        mahdoton_varasto = Varasto(10, 20)

        self.assertEqual(mahdoton_varasto.saldo, 10)

    def test_negatiivinen_lisays_ei_onnistu(self):
        self.varasto.lisaa_varastoon(-10)

        self.assertEqual(self.varasto.saldo, 0)

    def test_ei_voi_lisata_enemman_kuin_mahtuu(self):
        self.varasto.lisaa_varastoon(100)

        self.assertEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_ei_voi_poistaa_negatiivista_maaraa(self):
        maara = self.varasto.ota_varastosta(-10)

        self.assertEqual(maara, 0)

    def test_ei_voi_ottaa_enemman_kuin_on(self):
        self.varasto.lisaa_varastoon(10)

        maara= self.varasto.ota_varastosta(20)

        self.assertEqual(maara, 10)


    def test_str_on_oikein(self):
        self.assertEqual("saldo = 0, vielä tilaa 10", str(self.varasto))
