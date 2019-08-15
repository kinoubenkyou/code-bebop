Tags: concurrency

# Parallelism

A condition where two threads can run together at the same time. This requires a system with multiple processors or a multi-core processor.

# Concurrency

A condition where two threads can run in time period overlapping to each others. By this definition, parallelism is technically a particular case of concurrency. However, concurrency is usually considered in a system with a single-core processor. This process switch forth and back between the threads to run them.

# Global Interpreter Lock

A feature to prevent multi-threading parallelism. It ensures that, inside a process, only one thread can run at a time. It doesn't prevent switching between threads in a process though, thus doesn't prevent race condition.

Parallelism can still be achieved against GIL through multi-processing.

# Asynchronous

A condition where one thread doesn't wait for another thread to finish. This requires concurrency (or parallelism).
