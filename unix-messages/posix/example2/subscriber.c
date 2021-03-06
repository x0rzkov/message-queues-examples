#include <stdio.h>
#include <string.h>

#include <mqueue.h>

#define QUEUE_NAME "/queue2"

int main(void)
{
    mqd_t message_queue_id;
    char message_text[10000];
    unsigned int sender;
    int status;

    message_queue_id = mq_open(QUEUE_NAME, O_RDWR);
    if (message_queue_id == -1) {
        perror("Unable to open queue");
        return 2;
    }

    {
        struct mq_attr msgq_attr;
        mq_getattr(message_queue_id, &msgq_attr);
        printf("Queue: %s\n", QUEUE_NAME);
        printf("Max. messages:     %ld\n", msgq_attr.mq_maxmsg);
        printf("Current messages:  %ld\n", msgq_attr.mq_curmsgs);
        printf("Max. message size: %ld\n", msgq_attr.mq_msgsize);
    }

    status = mq_receive(message_queue_id, message_text, sizeof(message_text), &sender);
    if (status == -1) {
        perror("Unable to receive message");
        return 2;
    }
    printf("Received message (%d bytes) from %d: %s\n", status, sender, message_text);

    status = mq_close(message_queue_id);
    if (status == -1) {
        perror("Unable to close message queue");
        return 2;
    }

    return 0;
}
