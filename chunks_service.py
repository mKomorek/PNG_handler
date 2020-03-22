from model.ihdr_chunk import IHDRchunk

class ChunksService:

    def __init__(self, chunks_data):
        self.chunks_data = chunks_data
        self.chunk_tuples = []
        self.chunks = []
        self.parse_chunks_data()
        self.get_chunks()

    def chunk_iter(self):
        total_length = len(self.chunks_data)
        end = 8

        while (end  < total_length):     
            length = int.from_bytes(self.chunks_data[end : end + 4], 'big')
            begin_chunk_length = end
            begin_chunk_type = begin_chunk_length + 4
            begin_chunk_data = begin_chunk_type + 4
            begin_chunk_crc = begin_chunk_data + length
            end = begin_chunk_crc + 4

            yield ( self.chunks_data[begin_chunk_length: begin_chunk_type],
                    self.chunks_data[begin_chunk_type: begin_chunk_data],
                    self.chunks_data[begin_chunk_data: begin_chunk_crc],
                    self.chunks_data[begin_chunk_crc: end] )

    def parse_chunks_data(self):
        for chunk_length, chunk_type, chunk_data, chunk_crc in self.chunk_iter():
            chunk = (chunk_length, chunk_type, chunk_data, chunk_crc)
            self.chunk_tuples.append(chunk)

    def get_chunks(self):
        for chunk in self.chunk_tuples:
            if chunk[1].decode() == "IHDR":
                ihdr_chunk = IHDRchunk(chunk[0], chunk[2], chunk[3])
                self.chunks.append(ihdr_chunk)

    def display_chunks_type(self):
        print(" CHUNKS OF FILE ".center(50,'-'))
        for chunk in self.chunk_tuples:
            print("---> CHUNK TYPE: %s" % chunk[1].decode())
        print("".center(50, "-"))
        print("")

    def display_chunks_info(self):
        print("CHUNK DETAIL".center(50,'-'))
        for chunk in self.chunks:
            chunk.display_info()
