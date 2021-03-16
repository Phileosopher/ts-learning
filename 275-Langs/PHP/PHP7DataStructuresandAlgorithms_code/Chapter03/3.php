<?php

/* 
 * Example code for: PHP 7 Data Structures and Algorithms
 * 
 * Author: Mizanur rahman <mizanur.rahman@gmail.com>
 * 
 */

class ListNode {

    public $data = NULL;
    public $next = NULL;
    public $prev = NULL;

    public function __construct(string $data = NULL) {
        $this->data = $data;
    }

}

class DoublyLinkedList {

    private $_firstNode = NULL;
    private $_lastNode = NULL;
    private $_totalNode = 0;

    public function insertAtFirst(string $data = NULL) {
        $newNode = new ListNode($data);
        if ($this->_firstNode === NULL) {
            $this->_firstNode = &$newNode;
            $this->_lastNode = $newNode;
        } else {
            $currentFirstNode = $this->_firstNode;
            $this->_firstNode = &$newNode;
            $newNode->next = $currentFirstNode;
            $currentFirstNode->prev = $newNode;
        }
        $this->_totalNode++;
        return TRUE;
    }

    public function insertAtLast(string $data = NULL) {
        $newNode = new ListNode($data);
        if ($this->_firstNode === NULL) {
            $this->_firstNode = &$newNode;
            $this->_lastNode = $newNode;
        } else {
            $currentNode = $this->_lastNode;
            $currentNode->next = $newNode;
            $newNode->prev = $currentNode;
            $this->_lastNode = $newNode;
        }
        $this->_totalNode++;
        return TRUE;
    }

    public function insertBefore(string $data = NULL, string $query = NULL) {
        $newNode = new ListNode($data);

        if ($this->_firstNode) {
            $previous = NULL;
            $currentNode = $this->_firstNode;
            while ($currentNode !== NULL) {
                if ($currentNode->data === $query) {
                    $newNode->next = $currentNode;
                    $currentNode->prev = $newNode;
                    $previous->next = $newNode;
                    $newNode->prev = $previous;
                    $this->_totalNode++;
                    break;
                }
                $previous = $currentNode;
                $currentNode = $currentNode->next;
            }
        }
    }

    public function insertAfter(string $data = NULL, string $query = NULL) {
        $newNode = new ListNode($data);

        if ($this->_firstNode) {
            $nextNode = NULL;
            $currentNode = $this->_firstNode;
            while ($currentNode !== NULL) {
                if ($currentNode->data === $query) {
                    if ($nextNode !== NULL) {
                        $newNode->next = $nextNode;
                    }
                    if ($currentNode === $this->_lastNode) {
                        $this->_lastNode = $newNode;
                    }
                    $currentNode->next = $newNode;
                    $nextNode->prev = $newNode;
                    $newNode->prev = $currentNode;
                    $this->_totalNode++;
                    break;
                }
                $currentNode = $currentNode->next;
                $nextNode = $currentNode->next;
            }
        }
    }

    public function deleteFirst() {
        if ($this->_firstNode !== NULL) {
            if ($this->_firstNode->next !== NULL) {
                $this->_firstNode = $this->_firstNode->next;
                $this->_firstNode->prev = NULL;
            } else {
                $this->_firstNode = NULL;
            }
            $this->_totalNode--;
            return TRUE;
        }
        return FALSE;
    }

    public function deleteLast() {
        if ($this->_lastNode !== NULL) {

            $currentNode = $this->_lastNode;
            if ($currentNode->prev === NULL) {
                $this->_firstNode = NULL;
                $this->_lastNode = NULL;
            } else {
                $previousNode = $currentNode->prev;
                $this->_lastNode = $previousNode;
                $previousNode->next = NULL;
                $this->_totalNode--;
                return TRUE;
            }
        }
        return FALSE;
    }

    public function delete(string $query = NULL) {
        if ($this->_firstNode) {
            $previous = NULL;
            $currentNode = $this->_firstNode;
            while ($currentNode !== NULL) {
                if ($currentNode->data === $query) {
                    if ($currentNode->next === NULL) {
                        $previous->next = NULL;
                    } else {
                        $previous->next = $currentNode->next;
                        $currentNode->next->prev = $previous;
                    }

                    $this->_totalNode--;
                    break;
                }
                $previous = $currentNode;
                $currentNode = $currentNode->next;
            }
        }
    }

    public function displayForward() {
        echo "Total book titles: " . $this->_totalNode . "\n";
        $currentNode = $this->_firstNode;
        while ($currentNode !== NULL) {
            echo $currentNode->data . "\n";
            $currentNode = $currentNode->next;
        }
    }

    public function displayBackward() {
        echo "Total book titles: " . $this->_totalNode . "\n";
        $currentNode = $this->_lastNode;
        while ($currentNode !== NULL) {
            echo $currentNode->data . "\n";
            $currentNode = $currentNode->prev;
        }
    }

    public function getSize() {
        return $this->_totalNode;
    }

}

$BookTitles = new DoublyLinkedList();
$BookTitles->insertAtLast("Introduction to Algorithm");
$BookTitles->insertAtLast("Introduction to PHP and Data structures");
$BookTitles->insertAtLast("Programming Intelligence");
$BookTitles->insertAtFirst("Mediawiki Administrative tutorial guide");
$BookTitles->insertAfter("Introduction to Calculus", "Programming Intelligence");
$BookTitles->displayForward();
$BookTitles->displayBackward();
$BookTitles->deleteFirst();
$BookTitles->deleteLast();
$BookTitles->delete("Introduction to PHP and Data structures");
$BookTitles->displayForward();
$BookTitles->displayBackward();
//echo "2nd Item is: ".$BookTitles->getNthNode(2)->data;