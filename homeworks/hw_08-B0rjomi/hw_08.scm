; Вопрос 1
(define (reverse lst)
    (if (null? (cdr lst))
    lst
    (append (reverse (cdr lst)) (list (car lst))))
)

; Вопрос 2
(define (longest-increasing-subsequence lst)
    ;ТВОЙ КОД ЗДЕСЬ
    nil
)

(define (cadr s) (car (cdr s)))
(define (caddr s) (cadr (cdr s)))

; Дифференцирование
; derive возвращает производную EXPR по VAR
(define (derive expr var)
  (cond ((number? expr) 0)
        ((variable? expr) (if (same-variable? expr var) 1 0))
        ((sum? expr) (derive-sum expr var))
        ((product? expr) (derive-product expr var))
        ((exp? expr) (derive-exp expr var))
        (else 'Error)))

; переменные представляются символами
(define (variable? x) (symbol? x))
(define (same-variable? v1 v2)
  (and (variable? v1) (variable? v2) (eq? v1 v2)))

; числа сравниваются с помощью =
(define (=number? expr num)
  (and (number? expr) (= expr num)))

; суммы представляются списками, начинающимися с +.
(define (make-sum a1 a2)
  (cond ((=number? a1 0) a2)
        ((=number? a2 0) a1)
        ((and (number? a1) (number? a2)) (+ a1 a2))
        (else (list '+ a1 a2))))
(define (sum? x)
  (and (list? x) (eq? (car x) '+)))
(define (addend s) (cadr s))
(define (augend s) (caddr s))

; произведения представляются списками, начинающимися с *.
(define (make-product m1 m2)
  (cond ((or (=number? m1 0) (=number? m2 0)) 0)
        ((=number? m1 1) m2)
        ((=number? m2 1) m1)
        ((and (number? m1) (number? m2)) (* m1 m2))
        (else (list '* m1 m2))))
(define (product? x)
  (and (list? x) (eq? (car x) '*)))
(define (multiplier p) (cadr p))
(define (multiplicand p) (caddr p))

; Вопрос 3
(define (derive-sum expr var)
  (make-sum (derive (addend expr) var) (derive (augend expr) var))
)

; Вопрос 4
(define (derive-product expr var)
  (make-sum(make-product (derive (addend expr) var) (augend expr))
  (make-product (addend expr) (derive (augend expr) var)))
)

; Вопрос 5
; возведение в степень представляется списком, начинающимся с ^.
(define (make-exp base exponent)
  ;ТВОЙ КОД ЗДЕСЬ
  nil
)

(define (base exp)
  ;ТВОЙ КОД ЗДЕСЬ
  nil
)

(define (exponent exp)
  ;ТВОЙ КОД ЗДЕСЬ
  nil
)

(define (exp? exp)
  ;ТВОЙ КОД ЗДЕСЬ
  nil
)

(define x^2 (make-exp 'x 2))
(define x^3 (make-exp 'x 3))

; Вопрос 6
(define (derive-exp exp var)
  ;ТВОЙ КОД ЗДЕСЬ
  nil
)