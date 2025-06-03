import pyinputplus as pyip
import random, time

number_of_questions = 10
correct_answers = 0

min_val, max_val = 2, 9
difficulty = pyip.inputMenu(
    ['Easy', 'Medium', 'Hard'], numbered=True, prompt='Choose difficulty: '
)
if difficulty == 'Easy':
    min_val, max_val = 2, 9
elif difficulty == 'Medium':
    min_val, max_val = 11, 19
elif difficulty == 'Hard':
    min_val, max_val = 11, 39

for question_number in range(number_of_questions):
  num1 = random.randint(min_val, max_val)
  num2 = random.randint(min_val, max_val)

  prompt = '#%s: %s x %s = ' % (question_number, num1, num2)

  try:
    pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],
                          blockRegexes=[('.*', 'Incorrect!')],
                          timeout=8, limit=3)
  except pyip.TimeoutException:
    print('Out of time!')
  except pyip.RetryLimitException:
    print('Out of tries!')
  else:
    print('Correct!')
    correct_answers += 1
  finally:
    time.sleep(1)

print('Score: %s / %s' % (correct_answers, number_of_questions))