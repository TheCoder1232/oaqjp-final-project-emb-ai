from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        phrase_1 = "I am glad this happened"
        phrase_2 = "I am really mad about this"
        phrase_3 = "I feel disgusted just hearing about this"
        phrase_4 = "I am so sad about this"
        phrase_5 = "I am really afraid that this will happen"
        
        self.assertEqual(emotion_detector(phrase_1)['dominant_emotion'][0], 'joy')
        self.assertEqual(emotion_detector(phrase_2)['dominant_emotion'][0], 'anger')
        self.assertEqual(emotion_detector(phrase_3)['dominant_emotion'][0], 'disgust')
        self.assertEqual(emotion_detector(phrase_4)['dominant_emotion'][0], 'sadness')
        self.assertEqual(emotion_detector(phrase_5)['dominant_emotion'][0], 'fear')

if __name__ == "__main__":
    unittest.main()

