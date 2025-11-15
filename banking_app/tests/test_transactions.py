from banking_app.backend.transactions import TransactionManager


def test_record_transaction():
    tm = TransactionManager()
    txn = tm.record_transaction(1001, "DEPOSIT", 500)
    history = tm.get_history(1001)

    assert len(history) == 1
    assert history[0].txn_type == "DEPOSIT"
    assert history[0].amount == 500


def test_undo_transaction_stack():
    tm = TransactionManager()
    tm.record_transaction(1001, "DEPOSIT", 100)
    tm.record_transaction(1001, "WITHDRAW", 50)

    last_txn = tm.undo_last()
    assert last_txn.txn_type == "WITHDRAW"
    assert last_txn.amount == 50


def test_pending_queue():
    tm = TransactionManager()
    tm.add_pending(1001, "DEPOSIT", 300)
    tm.add_pending(1001, "WITHDRAW", 100)

    first = tm.process_next_pending()
    second = tm.process_next_pending()

    assert first.txn_type == "DEPOSIT"
    assert second.txn_type == "WITHDRAW"
