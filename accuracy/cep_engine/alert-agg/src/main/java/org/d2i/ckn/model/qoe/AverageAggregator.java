package org.d2i.ckn.model.qoe;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.extern.slf4j.Slf4j;

import java.time.Instant;
import java.time.ZoneId;
import java.time.format.DateTimeFormatter;

@Slf4j
@Data
@NoArgsConstructor
@AllArgsConstructor
public class AverageAggregator {
    private float average_req_accuracy = 0;
    private float average_req_delay = 0;
    private float total_events = 0;
    private float average_qoe = 0;
    private float average_qoe_delay = 0;
    private float average_qoe_acc = 0;
    private float average_pred_acc = 0;
    private float average_compute_time = 0;


    private String client_id = "";
    private String service_id = "";
    private String server_id = "";
    private String model = "";

    private long timestamp;

//    public String getFormattedTimestamp() {
//        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss.SSS").withZone(ZoneId.systemDefault());
//        return formatter.format(Instant.ofEpochMilli(timestamp));
//    }
}
