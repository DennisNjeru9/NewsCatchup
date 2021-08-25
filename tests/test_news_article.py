import unittest
from app.models import Article


class TestArticle(unittest.TestCase):
    
    def setUp(self):

        self.new_article = Article('reuters','Delta variant','The resurgence of the covid-19 pandemic','https://www.reuters.com/business/delta-variant/','https://www.reuters.com/resizer/-XuHVthViVkR3PtRLNdEZi1X1qI=/1200x628/smart/filters:quality(80)/cloudfront-us-east-2.images.arcpublishing.com/reuters/7O7MCYQ3P5IQVBKLFOFPD74GJE.jpg','2021-08-23T10:12:00Z')

    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

    
    def test_init(self):
        self.assertEqual(self.new_article.author,'reuters')
        self.assertEqual(self.new_article.title,'Delta variant')
        self.assertEqual(self.new_article.description,'The resurgence of the covid-19 pandemic')
        self.assertEqual(self.new_article.url,'https://www.reuters.com/business/delta-variant/')
        self.assertEqual(self.new_article.image,'https://www.reuters.com/resizer/-XuHVthViVkR3PtRLNdEZi1X1qI=/1200x628/smart/filters:quality(80)/cloudfront-us-east-2.images.arcpublishing.com/reuters/7O7MCYQ3P5IQVBKLFOFPD74GJE.jpg')
        self.assertEqual(self.new_article.publish_date,'2021-08-23T10:12:00Z')