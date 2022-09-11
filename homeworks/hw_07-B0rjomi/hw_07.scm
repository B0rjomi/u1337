; Вопрос 1
(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  ; ТВОЙ КОД ЗДЕСЬ
  (car (cdr s))
)

(define (caddr s)
  ; ТВОЙ КОД ЗДЕСЬ
  (car (cddr s))
)

; Вопрос 2
(define (sign x)
  ; ТВОЙ КОД ЗДЕСЬ
  (cond
    ((< x 0) -1)
    ((= x 0) 0)
    ((> x 0) 1))
)

; Вопрос 3
(define (square x) (* x x))

(define (pow b n)
  ; ТВОЙ КОД ЗДЕСЬ
  (cond
    ((= n 0) 1)
    ((even? n) (square (pow b (/ n 2))))
    ((odd? n) (* b (pow b (- n 1))))
    )
)

; Вопрос 4
(define (ordered? s)
  ; ТВОЙ КОД ЗДЕСЬ
  (if (or (null? s) (null? (cdr s)))
    #t
    (and (<= (car s) (cadr s)) (ordered? (cdr s)))
  )
)

; Вопрос 5
(define (empty? s) (null? s))

(define (add s v)
  ; ТВОЙ КОД ЗДЕСЬ
  (cond
    ((null? s) (list v))
    ((= (car s) v) s)
    ((> (car s) v) (cons v s))
    ((< (car s) v) (cons (car s) (add (cdr s) v)))
  )
  ; если 1-й элемент s == v  то вернуть s
  ; если 1-й элемент s > v то вернуть новый список где v стоит спереди s /(cons v s)/
  ; если 1-й элемент s < v то вернуть новый список где на первом месте стоит 1 элемент s (car s),
  ; и добавлять к нему (add (cdr s) v), пока перебор s не закончится
)

; Вопрос 6
(define (contains? s v)
  ; ТВОЙ КОД ЗДЕСЬ
  (cond
    ((empty? s) #f)
    ((> (car s) v) #f)
    ((= (car s) v) #t)
    (else (contains? (cdr s) v))
  )
)

; Эквивалентный код на Python:
;
; def empty(s):
;     return s is Link.empty
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)

; Вопрос 7
(define (intersect s t)
  ; ТВОЙ КОД ЗДЕСЬ
  (cond
    ((empty? s) nil)
    ((empty? t) nil)
    ((= (car s) (car t)) (cons (car s) (intersect (cdr s) (cdr t))))
    ((< (car s) (car t)) (intersect (cdr s) t))
    ((> (car s) (car t)) (intersect s (cdr t)))
  )
)

; Эквивалентный код на Python:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
  ; ТВОЙ КОД ЗДЕСЬ
  nil
)