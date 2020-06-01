from constants import TextColors, PNG_MAGIC_NUMBER
from model.ihdr_chunk import IHDRchunk
from model.plte_chunk import PLTEchunk
from model.idat_chunk import IDATchunk
from model.iend_chunk import IENDchunk
from model.ancillary_chunks import tIMEChunk, cHRMChunk, gAMAChunk

class ChunksService:

    def __init__(self, chunks_data):
        self.chunks_data = chunks_data
        self.chunks_type = []
        self.chunks = []
        self.idat_data_list = []
        self.parse_chunks_data()

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
            if chunk_type.decode() == "IHDR":
                self.ihdr_chunk = IHDRchunk(chunk_length, chunk_type, chunk_data, chunk_crc)
                self.chunks.append(self.ihdr_chunk)
            if chunk_type.decode() == "PLTE":
                plte_chunk = PLTEchunk(chunk_length, chunk_type, chunk_data, chunk_crc)
                self.chunks.append(plte_chunk)
            if chunk_type.decode() == "IDAT":
                idat_chunk = IDATchunk(chunk_length, chunk_type, chunk_data, chunk_crc, self.chunks[0].width, self.chunks[0].color_type)
                self.chunks.append(idat_chunk)
                self.idat_data_list.append(chunk_data)
            if chunk_type.decode() == "IEND":
                iend_chunk = IENDchunk(chunk_length, chunk_type, chunk_data, chunk_crc)
                self.chunks.append(iend_chunk)
            if chunk_type.decode() == "cHRM":
                chrm_chunk = cHRMChunk(chunk_length, chunk_type, chunk_data, chunk_crc)
                self.chunks.append(chrm_chunk)
            if chunk_type.decode() == "tIME":
                time_chunk = tIMEChunk(chunk_length, chunk_type, chunk_data, chunk_crc)
                self.chunks.append(time_chunk)
            if chunk_type.decode() == "gAMA":
                gAMA_chunk = gAMAChunk(chunk_length, chunk_type, chunk_data, chunk_crc)
                self.chunks.append(gAMA_chunk)
            self.chunks_type.append(chunk_type)

    def create_clean_file(self, file_name):
        critical_chunks = [b'IHDR', b'IDAT', b'IEND']
        if self.ihdr_chunk.color_type == 3:
            critical_chunks.insert(1, b'PLTE')

        new_file = open(file_name, 'wb')
        new_file.write(PNG_MAGIC_NUMBER)
        for chunk in self.chunks:
            if chunk.type in critical_chunks:
                new_file.write(chunk.length)
                new_file.write(chunk.type)
                new_file.write(chunk.data)
                new_file.write(chunk.crc)
        new_file.close()

    def parse_to_one_IDAT(self):
        data = b"".join(self.idat_data_list)
        idat_chunk = IDATchunk(b"", b"", data, b"", self.ihdr_chunk.width, self.ihdr_chunk.color_type)
        idat_chunk.data_parser()
        if idat_chunk.color_type == 3:
            idat_chunk.apply_palette(self.chunks[1].paletes)
        return idat_chunk

    def display_from_IDATs(self):
        idat_chunk = self.parse_to_one_IDAT()
        idat_chunk.display_image_from_recostrucrion_data()

    def display_chunks_type(self):
        print(TextColors.BOLD + TextColors.HEADER + " CHUNKS OF FILE ".center(50,'-') + TextColors.ENDC)
        for chunk_type in self.chunks_type:
            print("---> CHUNK TYPE: ", TextColors.setValueColor(chunk_type.decode()))
        print(TextColors.BOLD + TextColors.HEADER + "".center(50, "-") + TextColors.ENDC)
        print("")

    def display_chunks_info(self):
        print(TextColors.BOLD + TextColors.HEADER + " CHUNK DETAIL ".center(50,'-') + TextColors.ENDC)
        for chunk in self.chunks:
            chunk.display_info()
        print(TextColors.BOLD + TextColors.HEADER + "".center(50, "-") + TextColors.ENDC)
        print("")

    def make_encryption_ecb(self):
        idat_chunk = self.parse_to_one_IDAT()
        idat_chunk.encryption_ecb()
        idat_chunk.display_image_from_recostrucrion_data()

        idat_chunk.decryption_ecb()
        idat_chunk.display_image_from_recostrucrion_data()

    def make_encryption_cbc(self):
        idat_chunk = self.parse_to_one_IDAT()
        idat_chunk.encryption_cbc()
        idat_chunk.display_image_from_recostrucrion_data_encryption_cbc()

        idat_chunk.decryption_cbc()
        idat_chunk.display_image_from_recostrucrion_data()





