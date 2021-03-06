(ns durable-queue-3.core
  (:gen-class))

(require '[durable-queue :refer :all])
(require '[clojure.pprint :refer :all])

(defn -main
  [& args]
  (let [q (queues "/tmp" {})]
       (pprint (stats q))
       (put! q :queue-1 "task #A")
       (put! q :queue-1 "task #B")
       (put! q :queue-2 "task #C")
       (pprint (stats q))
       (println "Získávám dvě zprávy z front queue-1 a queue-2")
       (-> (take! q :queue-1) println)
       (-> (take! q :queue-2) println)
       (pprint (stats q))
       (println "Získávám další dvě zprávy z front queue-1 a queue-2")
       (-> (take! q :queue-1) println)
       (-> (take! q :queue-2) println)
       (pprint (stats q))))
