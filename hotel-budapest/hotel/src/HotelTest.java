import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class HotelTest {
    @Test
    public void testList() {
        Hotel hotel = new Hotel();
        assertEquals(101, hotel.list());
    }
}