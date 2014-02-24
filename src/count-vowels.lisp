;;; Counts the number of vowels in a word
;;; Enter your word with parentheses e.g., "hello"

(defun count-vowels (word)
  (count-if #'(lambda (i) (find i "aeiou")) word))
