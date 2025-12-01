from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation

class TopicModeler:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=100, stop_words='english')
        self.lda = LatentDirichletAllocation(n_components=5, random_state=42)
    
    def extract_topics(self, texts: list):
        if not texts:
            return []
        
        tfidf = self.vectorizer.fit_transform(texts)
        self.lda.fit(tfidf)
        
        feature_names = self.vectorizer.get_feature_names_out()
        topics = []
        
        for topic_idx, topic in enumerate(self.lda.components_):
            top_words = [feature_names[i] for i in topic.argsort()[-10:]]
            topics.append(top_words)
        
        return topics