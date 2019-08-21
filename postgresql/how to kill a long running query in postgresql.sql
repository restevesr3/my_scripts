SELECT * FROM pg_stat_activity WHERE state = 'active';

//polite way to stop
//SELECT pg_cancel_backend(PID);
SELECT pg_cancel_backend(4996);

//stop at all costs - can lead to full database restart
SELECT pg_terminate_backend(PID)