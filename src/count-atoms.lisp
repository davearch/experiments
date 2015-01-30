;;; David Archuleta

;;; Exercise 1.3 from 'Paradigms of Artificial Intelligence Programming:
;;; Write a function that counts the number of atoms in an expression.
;;; For example: (count-atoms '(a (b) c)) = 3. Notice that there is something
;;; of an ambiguity in this: should (a nil c) count as three atoms, or as two,
;;; because it is equivalent to (a () c)?

; I include this exercise to my public repository because (a) I spent a few
; hours doing it, and (b) my solution is pretty cool and requires just as few
; lines as Peter Norvig.

; Norvig's solution
(defun count-all-atoms (exp &optional (if-null 1))
  "Return the total number of atoms in the expression.
  counting nil as an atom only in non-tail position."
  (cond ((null exp) if-null)
	((atom exp) 1)
	(t (+ (count-all-atoms (first exp) 1)
	      (count-all-atoms (rest exp) 0)))))

; My Solution
(defun count-atoms (object)
  "Count number of atoms in an expression, including nils."
  (cond
    ((atom object) 1)
    ((consp object) (apply #'+ (mapcar #'count-atoms object)))
    (t 0)))

(count-atoms '(a b c))       ;; 3
(count-atoms '(1 2 3))       ;; 3
(count-atoms '(a (b) c))     ;; 3
(count-atoms '(a nil c))     ;; 3
(count-atoms '(a () c))      ;; 3
(count-atoms '(a ((a) b) a)) ;; 4
