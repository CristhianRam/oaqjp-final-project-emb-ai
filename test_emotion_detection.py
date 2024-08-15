import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestMyModule(unittest.TestCase):
    def test_emotion_detector(self):
        
        ans1 = emotion_detector("I am glad this happened")
        self.assertEqual(ans1["dominant_emotion"], "joy")

        ans2 = emotion_detector("I am really mad about this")
        self.assertEqual(ans2["dominant_emotion"], "anger")

        ans3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(ans3["dominant_emotion"], "disgust")

        ans4 = emotion_detector("I am so sad about this")
        self.assertEqual(ans4["dominant_emotion"], "sadness")

        ans5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(ans5["dominant_emotion"], "fear")

unittest.main()
