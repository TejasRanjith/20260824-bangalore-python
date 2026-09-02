def compile_feedback(ratings_dict):
    for key in ratings_dict:
        result = []
        for item in ratings_dict[key]:
            try:
                if type(item) == int:
                    result.append(float(item))
                else:
                    pass
            except:
                
        ratings_dict[key] = result
    print(ratings_dict)
                


feedback_data = {
    "Python Programming": [5, 4, "4", "Great", 5],
    "Machine Learning": [],
    "Deep Learning": ["Good", "Average", None]
}

compile_feedback(feedback_data)