def score_grade(score):
  if score <= 8:
    return 'tres faible'
  elif (score >= 8 and score <= 10):
    return 'faible'
  elif (score >= 10 and score <= 12):
    return 'passable'
  elif (score >= 12 and score <= 14):
    return 'assez bien'
  elif (score >= 14 and score <= 16):
    return 'bien'
  elif (score >= 16 and  score <=  18):
    return 'tres bien'
  elif score >= 18 :
    return 'excellent'
