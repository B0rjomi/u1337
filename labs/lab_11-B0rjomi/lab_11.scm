; Вопрос 3
(define (repeatedly-cube n x)
    (if (zero? n)
        x
        (let
            ((y (repeatedly-cube (- n 1) x)))
            (* y y y))))

; Вопрос 4
(define-macro (def func bindings body)
    `(define ,(cons func bindings) ,body)
)

; Вопрос 5
(define-macro (switch expr cases)
      ;ТВОЙ-КОД-ЗДЕСЬ
    nil
)

; Вопрос 6
(define (flatmap f x)
    ;ТВОЙ-КОД-ЗДЕСЬ
    nil)

(define (expand lst)
    ;ТВОЙ-КОД-ЗДЕСЬ
    nil)

(define (interpret instr dist)
    ;ТВОЙ-КОД-ЗДЕСЬ
    nil)

(define (apply-many n f x)
  (if (zero? n)
      x
      (apply-many (- n 1) f (f x))))

(define (dragon n d)
  (interpret (apply-many n expand '(f x)) d))