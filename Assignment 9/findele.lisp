
(setq m (read))
(setf numbers (make-array ' (m)))

(print "Enter 10 numbers :")

(dotimes (i m)
	(setf (aref numbers i) (read) )
)

(print "Enter postion of number to display ")

(setq num (read))

(dotimes (i m)
	(if  (= i num) (format t "Number is ~d" (aref numbers i)))		
)


