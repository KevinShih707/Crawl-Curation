import unittest
from ..src.corpora import Corpora
from ..src.lda import Lda
import numpy as np
import os
import math

class TestLda(unittest.TestCase):
    CSV_FILE_PATH = "DataProcessing/test_data/testData.csv"

    def setUp(self):
        self.corpora = Corpora(filePath = self.CSV_FILE_PATH, stopwords = "DataProcessing/src/stopwords.txt")
        self.lda = Lda(self.corpora, numTopics = 2, seed = 10)

    # def test_getTopicsStr(self):
    #     expectResult = [(0, '0.001*"來" + 0.001*"圖表" + 0.001*"你" + 0.001*"與" + 0.001*"讓" + 0.001*"在" + 0.001*"有" + 0.001*"吧" + 0.001*"圖" + 0.001*"也"'),
    #                     (1, '0.001*"圖表" + 0.001*"你" + 0.001*"在" + 0.001*"與" + 0.001*"覺化" + 0.001*"圖" + 0.001*"為" + 0.001*"台灣" + 0.001*"上" + 0.001*"呢"')]
    #     self.assertEqual(expectResult, self.lda.TopicsStr)

    # def test_getTopicsList(self):
    #     print(self.lda.TopicsList)
    #     expectResult = [[('0.001', '來'), ('0.001', '圖表'), ('0.001', '你'), ('0.001', '與'), ('0.001', '讓'), ('0.001', '在'), ('0.001', '有'), ('0.001', '吧'), ('0.001', '圖'), ('0.001', '也')],
    #                     [('0.001', '圖表'), ('0.001', '你'), ('0.001', '在'), ('0.001', '與'), ('0.001', '覺化'), ('0.001', '圖'), ('0.001', '為'), ('0.001', '台灣'), ('0.001', '上'), ('0.001', '呢')]]
    #     self.assertEqual(expectResult, self.lda.TopicsList)

    # def test_getTopicsListId(self):
    #     expectResult = [[(0.001, 53), (0.001, 290), (0.001, 9), (0.001, 151), (0.001, 190), (0.001, 114), (0.001, 135), (0.001, 61), (0.001, 289), (0.001, 51)],
    #                     [(0.001, 290), (0.001, 9), (0.001, 114), (0.001, 151), (0.001, 84), (0.001, 289), (0.001, 26), (0.001, 960), (0.001, 393), (0.001, 228)]]
    #     self.assertEqual(expectResult, self.lda.TopicsListId)

    # def test_topicsDistribution(self):
    #     from pprint import pprint
    #     pprint(self.lda.topicsDistribution(tfidf = self.corpora.TfidfPair)

    def test_saveModel(self):
        if(os.path.exists("DataProcessing/test_data/model_test.pkl")):
            os.remove("DataProcessing/test_data/model_test.pkl")
        self.assertFalse(os.path.exists("DataProcessing/test_data/model_test.pkl"))
        self.lda.saveModel("DataProcessing/test_data/model_test.pkl")
        self.assertTrue(os.path.exists("DataProcessing/test_data/model_test.pkl"))

    # def test_classifyTopic(self):
    #     expectResult = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1,
    #                     0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0,
    #                     0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1,
    #                     0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0,
    #                     1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1]
    #     self.assertEqual(expectResult, self.lda.classifyTopic())

    # def test_findArticleMatched(self):
    #     result = self.lda.findArticleMatched()
    #     self.assertEqual([0,  1,  2,  3,  4,  5,  7,  8,  9, 11], result[0][:10])
    #     self.assertEqual([6, 10, 13, 15, 17, 19, 22, 23, 24, 25], result[1][:10])
    #
    #     # self.assertEqual(result[0], self.lda.findArticleMatchd(0))
    #     # self.assertEqual(result[1], self.lda.findArticleMatchd(1))

    def test_relativeEntropy(self):
        p = [0.1, 0.2, 0.3, 0.4]
        q = [0.4, 0.3, 0.2, 0.1]
        r = [0.0, 0.1, 0.2, 0.3]
        self.assertEqual(0.0, self.lda._Lda__relativeEntropy(p, p))
        self.assertEqual(0.4564348191467835, self.lda._Lda__relativeEntropy(p, q))
        self.assertEqual(math.inf, self.lda._Lda__relativeEntropy(p, r))

    # def test_showRelativeEntropy(self):
    #     from pprint import pprint
    #     pprint (
    #     self.lda.showRelativeEntropy(1, self.corpora.DtMatrix)
    #     )

    # def test_showAuthenticArticle(self):
    #     print(
    #     self.lda.showAuthenticArticle(0, num = 3)
    #     )

if __name__ == "__main__":
    unittest.main()
