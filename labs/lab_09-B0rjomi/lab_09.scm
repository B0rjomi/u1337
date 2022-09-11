;; Scheme ;;

; Вопрос 2
(define (over-or-under x y)
  ;ТВОЙ-КОД-ЗДЕСЬ
  (cond
    ((> x y) 1)
    ((< x y) -1)
    ((= x y) 0)
  )
)

;;; Тесты
;(over-or-under 1 2)
; -1
;(over-or-under 2 1)
; 1
;(over-or-under 1 1)
; 0

; Вопрос 3
(define (filter f lst)
  ;ТВОЙ-КОД-ЗДЕСЬ
  (if (null? lst)
      lst
      (if (f (car lst))
          (cons (car lst) (filter f (cdr lst)))
          (filter f (cdr lst))))
)

;;; Тесты
;(define (even? x)
;  (= (modulo x 2) 0))
;(filter even? '(0 1 1 2 3 5 8))
; (0 2 8)

; Вопрос 4
(define (make-adder num)
  ;ТВОЙ-КОД-ЗДЕСЬ
  (define (sub-adder x)
    (+ num x))
  sub-adder
)

;;; Тесты
;(define adder (make-adder 5))
;(adder 8)
; 13

; Вопрос 5
(define lst
  ; ТВОЙ-КОД-ЗДЕСЬ
  (cons (cons 1 nil)
    (cons 2 (cons (cons 3 4)
      (cons 5 nil))))
)

; Вопрос 6
(define (composed f g)
  (define (h x)
    (f (g x))
  )
  h
)

; Вопрос 7
(define (remove item lst)
  ;ТВОЙ-КОД-ЗДЕСЬ
  (filter (lambda (x) (not(eq? item x)))
    lst
  )
)

;;; Тесты
;(remove 3 nil)
; ()
;(remove 3 '(1 3 5))
; (1 5)
;(remove 5 '(5 3 5 5 1 4 5 4))
; (3 1 4 4)

; Вопрос 8
(define (no-repeats s)
  ;ТВОЙ-КОД-ЗДЕСЬ
  nil
)

; Вопрос 9
(define (substitute s old new)
  ;ТВОЙ-КОД-ЗДЕСЬ
  nil
)

; Вопрос 10
(define (sub-all s olds news)
  ;ТВОЙ-КОД-ЗДЕСЬ
  nil
)